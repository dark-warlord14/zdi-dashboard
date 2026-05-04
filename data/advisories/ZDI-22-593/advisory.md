# ZDI-22-593: Bentley MicroStation CONNECT OBJ File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-593
- **ZDI-CAN:** ZDI-CAN-16172
- **Date:** 2022-04-12
- **CVE:** CVE-2022-28305
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** MicroStation CONNECT
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-593/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley MicroStation CONNECT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of OBJ files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/en/common-vulnerability-exposure/be-2022-0008

## Disclosure Timeline

- 2022-01-14 - Vulnerability reported to vendor
- 2022-04-12 - Coordinated public release of advisory
