# ZDI-21-187: Schneider Electric EcoStruxure Power Build SSD File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-187
- **ZDI-CAN:** ZDI-CAN-11850
- **Date:** 2021-02-10
- **CVE:** CVE-2021-22698
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Power Build
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-187/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric EcoStruxure Power Build. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SSD files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-012-01

## Disclosure Timeline

- 2020-09-04 - Vulnerability reported to vendor
- 2021-02-10 - Coordinated public release of advisory
