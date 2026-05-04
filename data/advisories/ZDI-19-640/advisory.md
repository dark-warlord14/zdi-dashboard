# ZDI-19-640: Google Android Bluetooth hci_len Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-640
- **ZDI-CAN:** ZDI-CAN-7860
- **Date:** 2019-07-08
- **CVE:** CVE-2019-9353
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Android
- **Credit:** Moony Li and Todd Han of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-640/
## Vulnerability Details

This vulnerability allows attackers in close proximity to execute arbitrary code on vulnerable installations of Google Android. User interaction is required to exploit this vulnerability in that the target must accept a malicious file transfer. The specific flaw exists within the parsing of Bluetooth packet lengths. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/17/19 - ZDI reported vulnerability to vendor 01/17/19 - The vendor acknowledged 01/17/19 - The vendor requested further information 01/28/19 - ZDI provided vendor the available details 01/28/19 - The vendor acknowledged 04/26/19 - ZDI requested an update from the vendor and reminded the vendor the case was due on May 17th 04/26/19 - The vendor replied the fix was ready and would be released with the next major version 06/06/19 - ZDI requested details for the fix release and notified the vendor the intention to 0-day should the fix not be available 06/07/19 - The vendor replied the fix was not public yet but would soon be included in the next release of a major version 08/20/19 - The vendor released a fix

## Disclosure Timeline

- 2019-01-17 - Vulnerability reported to vendor
- 2019-07-08 - Coordinated public release of advisory
- 2019-08-29 - Advisory Updated
