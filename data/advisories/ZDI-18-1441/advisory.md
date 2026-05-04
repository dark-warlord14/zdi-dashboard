# ZDI-18-1441: Horner Automation Cscape CSP File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1441
- **ZDI-CAN:** ZDI-CAN-6430
- **Date:** 2019-01-02
- **CVE:** CVE-2018-19005
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Horner Automation
- **Affected Products:** Cscape
- **Credit:** mdm and rgod of 9SG Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1441/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Horner Automation Cscape. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CSP files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Horner Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-354-01

## Disclosure Timeline

- 2018-07-17 - Vulnerability reported to vendor
- 2019-01-02 - Coordinated public release of advisory
- 2019-01-02 - Advisory Updated
