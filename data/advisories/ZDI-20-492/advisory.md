# ZDI-20-492: Eaton HMiSoft VU3 File Parsing wDescribeLen Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-492
- **ZDI-CAN:** ZDI-CAN-10417
- **Date:** 2020-04-15
- **CVE:** CVE-2020-10637
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Eaton
- **Affected Products:** HMiSoft
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-492/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Eaton HMiSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of wDescribeLen information within VU3 files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Eaton has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-105-01

## Disclosure Timeline

- 2020-02-12 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
