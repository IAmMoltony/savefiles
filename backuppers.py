from backupper_minecraft import MinecraftBackupper
from backupper_touhou import Touhou06Backupper, Touhou07Backupper, Touhou08Backupper
from backupper_babaisyou import BabaIsYouBackupper
from backupper_supertux import SuperTuxBackupper
from backupper_forager import ForagerBackupper

BACKUPPERS = {
    "Minecraft": MinecraftBackupper,
    "Touhou06": Touhou06Backupper,
    "Touhou07": Touhou07Backupper,
    "Touhou08": Touhou08Backupper,
    "BabaIsYou": BabaIsYouBackupper,
    "SuperTux": SuperTuxBackupper,
    "Forager": ForagerBackupper
}
