# ZDI-19-690: Fuji Electric FRENIC Loader FN1 File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-690
- **ZDI-CAN:** ZDI-CAN-7921
- **Date:** 2019-08-05
- **CVE:** CVE-2019-13512
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Fuji Electric
- **Affected Products:** FRENIC Loader
- **Credit:** kimiya of 9SG Security Team - kimiya@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-690/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Fuji Electric FRENIC Loader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FN1 files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-213-02

## Disclosure Timeline

- 2019-03-06 - Vulnerability reported to vendor
- 2019-08-05 - Coordinated public release of advisory
