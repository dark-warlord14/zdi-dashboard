# ZDI-22-225: Bentley MicroStation CONNECT DGN File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-225
- **ZDI-CAN:** ZDI-CAN-15510
- **Date:** 2022-01-31
- **CVE:** CVE-2021-46638
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** MicroStation CONNECT
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-225/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley MicroStation CONNECT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DGN files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/en/common-vulnerability-exposure/BE-2021-0009

## Disclosure Timeline

- 2021-10-06 - Vulnerability reported to vendor
- 2022-01-31 - Coordinated public release of advisory
