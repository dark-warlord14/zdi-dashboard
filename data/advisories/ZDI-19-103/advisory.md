# ZDI-19-103: OMRON CX-Supervisor sr3 File Parsing WriteMessage Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-103
- **ZDI-CAN:** ZDI-CAN-6639
- **Date:** 2019-01-19
- **CVE:** CVE-2018-19015
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-Supervisor
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-103/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on vulnerable installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of project files. The issue results from the lack of proper validation of a user-supplied string, which can lead to arbitrary file creation. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-017-01

## Disclosure Timeline

- 2018-07-06 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
