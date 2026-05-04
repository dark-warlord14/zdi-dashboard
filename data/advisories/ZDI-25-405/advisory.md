# ZDI-25-405: Fuji Electric Smart Editor X1 File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-405
- **ZDI-CAN:** ZDI-CAN-26024
- **Date:** 2025-06-17
- **CVE:** CVE-2025-41388
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Smart Editor
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-405/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Smart Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of X1 files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-168-04

## Disclosure Timeline

- 2025-02-21 - Vulnerability reported to vendor
- 2025-06-17 - Coordinated public release of advisory
- 2025-06-17 - Advisory Updated
