# ZDI-19-173: OMRON CX-Supervisor SCS File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-173
- **ZDI-CAN:** ZDI-CAN-7464
- **Date:** 2019-02-08
- **CVE:** CVE-2018-19020
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Omron
- **Affected Products:** CX-Supervisor
- **Credit:** Michael DePlante of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-173/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SCS files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-017-01

## Disclosure Timeline

- 2018-11-08 - Vulnerability reported to vendor
- 2019-02-08 - Coordinated public release of advisory
