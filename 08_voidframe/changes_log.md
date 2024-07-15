# Version Updates
 * Updated to 3.12 Gigas / ACOT

# District Functionality Changes
 * Foundry: IF the frame is nanite ascended, foundry districts have nanite upkeep but produce extra flat alloys
 * Temple: Uses the new DM ACOT priest jobs (these did not exist beforehand)
 * Simulation: Gets extra jobs if virtual ascended
 * Research: Gets extra jobs if virtual ascended
 * Fortress: Uses new ACOT soldier jobs

# Under the Hood Stuff
 * Updated vanilla gigas districts to use new inline code for job swapping

# Bug Fixes
 * Fixed DM Maginot districts not being buildable if AOT isn't loaded
 * Fixed an scope problem at acot_pmc.13 when it calls acot_pmc.1301 (bug came from AOT).