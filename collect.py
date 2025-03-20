from subprocess import run
from os import environ
from pathlib import Path

def detect():
	cpu = None
	os = None
	uname = run(["uname -ar"], shell=True, capture_output=True, text=True).stdout
	if("Darwin" in uname):
		os = "Mac"
	if("Linux" in uname):
		os = "Linux"

	if(os == "Mac"):
		if("arm" in uname):
			cpu = "ARM"
		else:
			cpu = "Intel"
	if(os == "Linux"):
		cpuinfo = run(["cat /proc/cpuinfo"], shell=True, capture_output=True, text=True).stdout
		if("AMD" in cpuinfo):
			cpu = "AMD"
		if("Intel" in cpuinfo):
			cpu = "Intel"
		if("BogoMIPS" in cpuinfo):
			cpu = "ARM"
	return cpu, os

def main():
	cpu, os = detect()
	dir = Path(__file__).parent
	with open(dir / "target_cpu", "w") as f:
		f.write(f"{cpu}")
	with open(dir / "target_os", "w") as f:
		f.write(f"{os}")


if __name__ == "__main__":
	main()