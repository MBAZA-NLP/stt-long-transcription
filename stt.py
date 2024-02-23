import nemo.collections.asr as nemo_asr
from nemo.collections.asr.parts.utils.streaming_utils import FrameBatchASR
import math
from omegaconf import OmegaConf,open_dict                                                                            
import copy


def transcribe_long_audios(filename,model_name):
    asr_model=model_name
    model_stride = 4
    batch_size = 1
    total_buffer_in_secs = 30.0
    chunk_len_in_ms = 22000 # this means the the context size is 8 seconds, 4s for the left and right context
    cfg = copy.deepcopy(asr_model._cfg)
    OmegaConf.set_struct(cfg.preprocessor, False)
    cfg.preprocessor.dither = 0.0
    cfg.preprocessor.pad_to = 0
    OmegaConf.set_struct(cfg.preprocessor, True)
    asr_model.eval()
    asr_model = asr_model.to(asr_model.device)
    feature_stride = cfg.preprocessor['window_stride']
    model_stride_in_secs = feature_stride * model_stride
    total_buffer = total_buffer_in_secs
    chunk_len = chunk_len_in_ms / 1000
    tokens_per_chunk = math.ceil(chunk_len / model_stride_in_secs)
    mid_delay = math.ceil((chunk_len + (total_buffer - chunk_len) / 2) / model_stride_in_secs)

    frame_asr = FrameBatchASR(
            asr_model=asr_model, frame_len=chunk_len, total_buffer=total_buffer_in_secs, batch_size=batch_size,
        )
    frame_asr.read_audio_file(filename, mid_delay, model_stride_in_secs)
    transcription = frame_asr.transcribe(tokens_per_chunk,mid_delay)
    return transcription