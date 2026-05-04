# ZDI-23-1170: (Pwn2Own) HP LaserJet Pro M479fdw bksettings Hardcoded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1170
- **ZDI-CAN:** ZDI-CAN-19693
- **Date:** 2023-08-24
- **CVE:** CVE-2023-35176
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** Color LaserJet Pro M479fdw
- **Credit:** Nguyen Cong Thanh - @ExLuck99 and Ha Anh Hoang - @hoangha2
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1170/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of HP LaserJet Pro M479fdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Backup and Restore functionality. The issue results from a hardcoded crytographic key. An attacker can leverage this vulnerability to bypass authentication and execute arbitrary code in the context of the device.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_8651671-8651697-16/hpsbpi03852

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
