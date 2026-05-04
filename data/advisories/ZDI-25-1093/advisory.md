# ZDI-25-1093: (0Day) PDFsam Enhanced Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1093
- **ZDI-CAN:** ZDI-CAN-27867
- **Date:** 2025-12-11
- **CVE:** CVE-2025-14405
- **CVSS:** 6.6
- **CVSS Vector:** AV:P/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDFsam
- **Affected Products:** Enhanced
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1093/
## Vulnerability Details

This vulnerability allows phyiscally-present attackers to escalate privileges on affected installations of PDFsam Enhanced. An attacker must first obtain the ability to mount a malicious drive onto the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

08/14/25 - ZDI reported the vulnerability to the vendor 08/15/25 – the vendor acknowledged the receipt of the report 09/23/25 - ZDI asked for updates 11/10/25 - ZDI asked for updates 12/04/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/11/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-14 - Vulnerability reported to vendor
- 2025-12-11 - Coordinated public release of advisory
- 2025-12-11 - Advisory Updated
