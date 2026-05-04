# ZDI-08-054: Multiple Vendor libpurple MSN Protocol SLP Message Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-054
- **ZDI-CAN:** ZDI-CAN-338
- **Date:** 2008-08-28
- **CVE:** CVE-2008-2927
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adium, Pidgin
- **Affected Products:** Adiumx, Pidgin
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-054/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of messaging applications that make use of the libpurple library. User interaction is not required to exploit this vulnerability. The specific flaw exists in the implementation of the MSN protocol, specifically the handling of SLP messages. The function msn_slplink_process_msg() fails to properly validate an offset value specified in the SLP packet. By providing a specific value, an attacker can overflow a heap buffer resulting in arbitrary code execution.

## Additional Details

Pidgin has issued an update to correct this vulnerability. More details can be found at: http://www.pidgin.im/news/security/?id=25

## Disclosure Timeline

- 2008-05-27 - Vulnerability reported to vendor
- 2008-08-28 - Coordinated public release of advisory
