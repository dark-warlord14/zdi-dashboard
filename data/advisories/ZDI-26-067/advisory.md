# ZDI-26-067: Docker Desktop for Windows Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-067
- **ZDI-CAN:** ZDI-CAN-28190
- **Date:** 2026-02-05
- **CVE:** CVE-2025-14740
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Nitesh Surana (niteshsurana.com) and Amol Dosanjh of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-067/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop for Windows. User interaction on the part of an administrator is required to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions on a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

Fixed in version 4.57.0 https://docs.docker.com/desktop/release-notes/

## Disclosure Timeline

- 2025-11-14 - Vulnerability reported to vendor
- 2026-02-05 - Coordinated public release of advisory
- 2026-02-05 - Advisory Updated
