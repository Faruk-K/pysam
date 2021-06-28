import sys
from typing import List, Union, NoReturn, Iterable, Any, Tuple, Optional
if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

class _HasFileNo(Protocol):
    def fileno(self) -> int: ...

def get_verbosity() -> int: ...
def set_verbosity(level: int): ...

class HFile:
    def __init__(self, name: Union[int, str], mode: str = ...) -> None: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, type, value, tb): ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> str: ...
    @property
    def closed(self) -> bool: ...
    @property
    def mode(self) -> str: ...
    @property
    def name(self) -> Union[int, str]: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def read(self, size: int = ...) -> bytes: ...
    def readall(self) -> bytes: ...
    def readinto(self, buf: Any) -> bytes: ...
    def readline(self, size: int = ...) -> bytes: ...
    def readlines(self) -> List[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, *args) -> NoReturn: ...
    def writable(self) -> bool: ...
    def write(self, b: bytes) -> int: ...
    def writelines(self, lines: Iterable[bytes]) -> None: ...

class HTSFile:
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    @property
    def filename(self) -> Any: ...
    @property
    def mode(self) -> str: ...
    @property
    def threads(self) -> int: ...
    @property
    def index_filename(self) -> Optional[str]: ...
    @property
    def is_stream(self) -> bool: ...
    @property
    def is_remote(self) -> bool: ...
    @property
    def duplicate_filehandle(self) -> bool: ...
    def close(self) -> None: ...
    def check_truncation(self, ignore_truncation: bool = ...) -> None: ...
    @property
    def category(self) -> str: ...
    @property
    def format(self) -> str: ...
    @property
    def version(self) -> Tuple[int, int]: ...
    @property
    def compression(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def is_open(self) -> bool: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def closed(self) -> bool: ...
    @property
    def is_write(self) -> bool: ...
    @property
    def is_read(self) -> bool: ...
    @property
    def is_sam(self) -> bool: ...
    @property
    def is_bam(self) -> bool: ...
    @property
    def is_cram(self) -> bool: ...
    @property
    def is_vcf(self) -> bool: ...
    @property
    def is_bcf(self) -> bool: ...
    def reset(self) -> None: ...
    def seek(self, offset: int) -> int: ...
    def tell(self) -> int: ...
    def add_hts_options(self, format_options: Optional[List[str]] = ...) -> None: ...
    def parse_region(
        self,
        contig: Optional[str] = ...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
        region: Optional[str] = ...,
        tid: Optional[int] = ...,
        reference: Optional[str] = ...,
        end: Optional[int] = ...,
    ) -> Tuple[int, int, int, int]: ...
    def is_valid_tid(self, tid: int) -> bool: ...
    def is_valid_reference_name(self, contig: str) -> bool: ...
    def get_tid(self, contig: str) -> int: ...
    def get_reference_name(self, tid: int) -> Optional[str]: ...
