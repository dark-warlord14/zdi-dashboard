# ZDI-18-1442: Horner Automation Cscape CSP File Parsing Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1442
- **ZDI-CAN:** ZDI-CAN-6431
- **Date:** 2019-01-02
- **CVE:** CVE-2018-19005
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Horner Automation
- **Affected Products:** Cscape
- **Credit:** mdm and rgod of 9SG Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1442/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Horner Automation Cscape. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CSP files. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Horner Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-354-01

## Disclosure Timeline

- 2018-07-17 - Vulnerability reported to vendor
- 2019-01-02 - Coordinated public release of advisory
- 2019-01-02 - Advisory Updated
