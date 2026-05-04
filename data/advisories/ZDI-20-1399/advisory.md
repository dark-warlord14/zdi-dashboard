# ZDI-20-1399: (0Day) Realtek RTL8811AU Wi-Fi Driver rtwlanu Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1399
- **ZDI-CAN:** ZDI-CAN-10715
- **Date:** 2020-12-07
- **CVE:** N/A
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Realtek
- **Affected Products:** RTL8811AU
- **Credit:** Haikuo Xie 、Ying Wang and Ye zhang of Baidu Security LabL
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1399/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of the Realtek RTL8811AU Wi-Fi driver. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of 802.11 frames. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/24/20 – ZDI reported the vulnerability to the vendor 10/07/20 – ZDI requested an update 10/28/20 – The vendor indicated they were working on a fix 11/09/20 – The vendor indicated they would provide a fix with the next update 11/09/20 – ZDI requested an ETA for the fix 11/17/20 – The vendor indicated the fix would be available on 11/27/20 11/23/20 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisories on 11/30/20 if no update was published -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-06-24 - Vulnerability reported to vendor
- 2020-12-07 - Coordinated public release of advisory
