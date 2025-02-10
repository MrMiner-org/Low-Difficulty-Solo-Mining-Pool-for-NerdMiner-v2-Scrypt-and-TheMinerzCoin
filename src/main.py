from src.pool_logic import Pool
from src.ai_manager import AIManager
from src.block_notifier import BlockNotifier
from src.payout_manager import PayoutManager
import threading

def main():
    # Start core pool logic
    pool = Pool()
    threading.Thread(target=pool.start, daemon=True).start()

    # Start AI optimization cycle
    ai_manager = AIManager()
    threading.Thread(target=ai_manager.run_cycle, daemon=True).start()

    # Start block notifications monitoring (Discord/Telegram)
    notifier = BlockNotifier()
    threading.Thread(target=notifier.monitor, daemon=True).start()

    # Schedule weekly payouts (blocking call for demo purposes)
    payout_manager = PayoutManager()
    payout_manager.schedule_weekly_payouts()

if __name__ == "__main__":
    main()
