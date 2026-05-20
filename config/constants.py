

# =========================
# APP BRANDING
# =========================

APP_NAME = "RoleRadar"

APP_TAGLINE = (
    "Track applications, analyze resumes, "
    "and turn job search activity into career intelligence."
)


# =========================
# PAGE NAVIGATION
# =========================

NAVIGATION_PAGES = [
    "Command Center",
    "Radar Lab",
    "Help"
]


# =========================
# APPLICATION STATUS OPTIONS
# =========================

APPLICATION_STATUSES = [
    "Applied",
    "Interviewing",
    "Rejected",
    "Offer"
]

FILTER_STATUS_OPTIONS = [
    "All",
    "Applied",
    "Interviewing",
    "Rejected",
    "Offer"
]


# =========================
# WORK ARRANGEMENT OPTIONS
# =========================

WORK_ARRANGEMENTS = [
    "Not Specified",
    "Remote",
    "Hybrid",
    "On-site"
]


# =========================
# FOLLOW-UP TYPES
# =========================

FOLLOW_UP_TYPES = [
    "Post-Application Follow-Up",
    "Interview Thank You",
    "Recruiter Networking Message"
]


# =========================
# APPLICATION DATA COLUMNS
# =========================

APPLICATION_COLUMNS = [
    "Date Added",
    "Company",
    "Role",
    "Location",
    "Work Arrangement",
    "Status",
    "Job Link",
    "Notes"
]


# =========================
# ROLE RADAR SCORE LABELS
# =========================

FIT_LABELS = {
    "excellent": "Excellent Fit",
    "strong": "Strong Fit",
    "moderate": "Moderate Fit",
    "weak": "Weak Fit"
}


# =========================
# ANALYSIS HISTORY LIMITS
# =========================

MAX_ANALYSIS_HISTORY = 10


# =========================
# DEFAULT UI MESSAGES
# =========================

EMPTY_APPLICATION_MESSAGE = (
    "No applications tracked yet."
)

EMPTY_ANALYSIS_HISTORY_MESSAGE = (
    "No resume analysis history available yet."
)

NO_SKILLS_FOUND_MESSAGE = (
    "RoleRadar could not confidently detect major skill matches."
)