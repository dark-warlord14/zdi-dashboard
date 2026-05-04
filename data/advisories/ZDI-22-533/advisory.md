# ZDI-22-533: (Pwn2Own) HP LaserJet Pro MFP M283fdw eContactRestore Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-533
- **ZDI-CAN:** ZDI-CAN-15896
- **Date:** 2022-03-23
- **CVE:** CVE-2022-24293
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** LaserJet Pro MFP M283fdw
- **Credit:** Alexander Bolshev (@dark_k3y), Timo Hirvonen (@TimoHirvonen), and Dmitry Janushkevich (@InfoSecDJ)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-533/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of HP LaserJet Pro MFP M283fdw printers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the address book feature. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

https://support.hp.com/us-en/document/ish_5950417-5950443-16/hpsbpi03781

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
