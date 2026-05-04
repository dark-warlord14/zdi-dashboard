# ZDI-06-001: Clam AntiVirus UPX Unpacking Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-001
- **ZDI-CAN:** ZDI-CAN-011
- **Date:** 2006-01-12
- **CVE:** CVE-2006-0162
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Clam AntiVirus
- **Affected Products:** Clam AntiVirus
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable Clam AntiVirus installations. Authentication is not required to exploit this vulnerability. This specific flaw exists within libclamav/upx.c during the unpacking of executable files compressed with UPX. Due to an invalid size calculation during a data copy from the user-controlled file to heap allocated memory, an exploitable memory corruption condition is created.

## Additional Details

Addressed in Clam AntiVirus version 0.88: http://sf.net/project/shownotes.php?release_id=384086&group_id=86638

## Disclosure Timeline

- 2005-12-13 - Vulnerability reported to vendor
- 2006-01-12 - Coordinated public release of advisory
