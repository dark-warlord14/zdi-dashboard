# ZDI-20-1239: (0Day) Realtek rtl81xx SDK Wi-Fi Driver rtwlanu Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1239
- **ZDI-CAN:** ZDI-CAN-10180
- **Date:** 2020-10-08
- **CVE:** N/A
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Realtek
- **Affected Products:** rtl81xx SDK
- **Credit:** Haikuo Xie ,Ying Wang of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1239/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Realtek rtl81xx SDK Wi-Fi driver. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of 802.11 frames. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/11/20 - ZDI reported the vulnerability to the vendor 05/13/20 – The vendor confirmed receipt of the report and requested more technical details 05/13/20 - ZDI clarified that the technical details are included in the report 08/18/20 - ZDI contacted the vendor requesting a status update 09/09/20 - ZDI requested an update 10/01/20 - ZDI notified the vendor of the intention to publish these reports as 0-day advisories on 10/08/2020 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-04-29 - Vulnerability reported to vendor
- 2020-10-08 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
