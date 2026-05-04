# ZDI-20-289: (Pwn2Own) Xiaomi Mi9 Browser manualUpgradeInfo Improper Control of Generation of Code Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-289
- **ZDI-CAN:** ZDI-CAN-9665
- **Date:** 2020-03-12
- **CVE:** CVE-2020-9530
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** @fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-289/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Xiaomi Mi9 Browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of manualUpgradeInfo objects. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in v11.0.1.54

## Disclosure Timeline

- 2019-11-21 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
