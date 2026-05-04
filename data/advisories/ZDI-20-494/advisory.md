# ZDI-20-494: Intel Wi-Fi Link Driver Netwtw04 Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-494
- **ZDI-CAN:** ZDI-CAN-9277
- **Date:** 2020-04-15
- **CVE:** CVE-2020-0558
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Intel
- **Affected Products:** Wi-Fi Link Driver
- **Credit:** Haikuo Xie and Ying Wang of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-494/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Intel Wi-Fi Link Driver. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of 802.11 frames. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Intel has issued an update to correct this vulnerability. More details can be found at: https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00338.html

## Disclosure Timeline

- 2019-11-27 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
