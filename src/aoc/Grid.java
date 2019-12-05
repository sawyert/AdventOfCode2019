package aoc;

import java.util.Arrays;

public class Grid {
	private static final int size = 30000;

	private final short[][] innergrid = new short[Grid.size][Grid.size];

	public Grid() {
		for (final short[] row : this.innergrid) {
			final short initial = 0;
			Arrays.fill(row, initial);
		}
	}

	public String intersections() {
		final StringBuffer lReturn = new StringBuffer();

		for (int i = 0; i < Grid.size; i++) {
			for (int j = 0; j < Grid.size; j++) {
				final int value = this.innergrid[i][j];
				if (value > 1) {
					final int distance = Math.abs(i - 10000) + Math.abs(j - 10000);
					lReturn.append(i + "," + j + " = " + distance + "\n");
				}
			}
		}

		return lReturn.toString();
	}

	public void plotline(int startx, int starty, String instructions) {
		final String[] args = instructions.split(",");
		int x = startx;
		int y = starty;
		for (String arg : args) {
			arg = arg.trim();
			final String direction = arg.substring(0, 1);
			final String length = arg.substring(1);

			int counter = Integer.parseInt(length);
			while (counter > 0) {
				this.innergrid[x][y] += 1;

				switch (direction) {
				case "U":
					y += 1;
					break;
				case "D":
					y -= 1;
					break;
				case "R":
					x += 1;
					break;
				case "L":
					x -= 1;
					break;
				}
				counter -= 1;
			}
		}
	}
}
