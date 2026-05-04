# ZDI-22-349: (Pwn2Own) Western Digital My Cloud Pro Series PR4100 ConnectivityService Insufficient Verification of Data Authenticity Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-349
- **ZDI-CAN:** ZDI-CAN-15859
- **Date:** 2022-02-15
- **CVE:** CVE-2022-22994
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Martin Rakhmanov (@mrakhmanov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-349/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ConnectivityService service. The issue results from the lack of proper authentication of data received via HTTP. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-22002-my-cloud-os5-firmware-5-19-117

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
