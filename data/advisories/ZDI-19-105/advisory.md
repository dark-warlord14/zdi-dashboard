# ZDI-19-105: OMRON CX-Supervisor sr3 File Parsing DeleteFile Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-105
- **ZDI-CAN:** ZDI-CAN-6646
- **Date:** 2019-01-19
- **CVE:** CVE-2018-19013
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-Supervisor
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-105/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of project files. The issue results from the lack of proper validation of a user-supplied string, allowing for the deletion of any file on the system. An attacker could use this to delete data or create a denial-of-service condition.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-017-01

## Disclosure Timeline

- 2018-07-06 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
