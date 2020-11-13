import argparse

def main(args):
    pass
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create printable calendars.')
    parser.add_argument('--type', type=str, nargs=1, choices=['MonthlyLandscape'], default='MonthlyLandscape',
                    help='Type of calendar',)
    parser.add_argument('--year', type=int, nargs=1, default=2020,
                                        help='Start year')
    parser.add_argument('--month', type=int, nargs=1, default=1,
                                        help='Start month')
    parser.add_argument('--day', type=int, nargs=1, default=1,
                                        help='Start day')
    parser.add_argument('--cnt', type=int, nargs=1, default=1,
                                        help='Number of calendars')
    parser.add_argument('--startday', type=str, nargs=1, default=6,
                                        help='For monthly calendars, the day on which to start, default Sunday (6). Mon, Tues, Wed... is 0, 1, 2...',
                                        choices=[0, 1, 2, 3, 4, 5, 6])


    args = parser.parse_args()
    main()