# ZDI-18-1252: LAquis SCADA LQS File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1252
- **ZDI-CAN:** ZDI-CAN-6373
- **Date:** 2018-10-16
- **CVE:** CVE-2018-17899
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1252/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of LAquis SCADA Software. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-289-01

## Disclosure Timeline

- 2018-06-22 - Vulnerability reported to vendor
- 2018-10-16 - Coordinated public release of advisory
- 2018-10-16 - Advisory Updated
