# ZDI-09-031: Multiple Vendor libpurple MSN Protocol SLP Message Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-031
- **ZDI-CAN:** ZDI-CAN-424
- **Date:** 2009-06-08
- **CVE:** CVE-2009-1376
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adium, Pidgin
- **Affected Products:** Adiumx, Pidgin
- **Credit:** Loic VALBON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of messaging applications that make use of the libpurple library. User interaction is not required to exploit this vulnerability. The specific flaw exists in the implementation of the MSN protocol, specifically the handling of SLP messages. The function msn_slplink_process_msg() fails to properly validate an offset value specified in the SLP packet. By providing a specific value, an attacker can overflow a heap buffer resulting in arbitrary code execution.

## Additional Details

Pidgin has issued an update to correct this vulnerability. More details can be found at: http://pidgin.im/news/security/?id=32

## Disclosure Timeline

- 2009-02-25 - Vulnerability reported to vendor
- 2009-06-08 - Coordinated public release of advisory
