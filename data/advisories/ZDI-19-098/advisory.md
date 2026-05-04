# ZDI-19-098: LAquis SCADA LQS File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-098
- **ZDI-CAN:** ZDI-CAN-7113
- **Date:** 2019-01-19
- **CVE:** CVE-2018-19004
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** LAquis
- **Affected Products:** SCADA
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-098/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of LAquis SCADA Software. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of LQS files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the aq process.

## Additional Details

LAquis has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-08-13 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
