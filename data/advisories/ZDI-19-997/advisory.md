# ZDI-19-997: OMRON CX-Supervisor Vulnerable Third-Party Component Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-997
- **ZDI-CAN:** ZDI-CAN-9313
- **Date:** 2019-12-09
- **CVE:** CVE-2019-18251
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-Supervisor
- **Credit:** Michael DePlante
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-997/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Teamviewer that is installed with Omron CX-Supervisor. The issue results from the use of an outdated version of Teamviewer containing known vulnerabilities. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-318-04

## Disclosure Timeline

- 2019-08-22 - Vulnerability reported to vendor
- 2019-12-09 - Coordinated public release of advisory
