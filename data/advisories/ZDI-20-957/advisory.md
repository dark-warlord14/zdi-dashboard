# ZDI-20-957: Advantech WebAccess/HMI Designer PM3 File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-957
- **ZDI-CAN:** ZDI-CAN-10134
- **Date:** 2020-08-10
- **CVE:** CVE-2020-16211
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/HMI Designer
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-957/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WebAccess/HMI Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PM3 files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-219-02

## Disclosure Timeline

- 2020-02-18 - Vulnerability reported to vendor
- 2020-08-10 - Coordinated public release of advisory
