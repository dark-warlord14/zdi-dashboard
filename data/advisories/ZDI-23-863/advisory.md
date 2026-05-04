# ZDI-23-863: (0Day) Ashlar-Vellum Cobalt Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-863
- **ZDI-CAN:** ZDI-CAN-17987
- **Date:** 2023-06-15
- **CVE:** CVE-2023-34303
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-863/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VC6 files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/22/22 – The ZDI asked for a Vendor PSIRT contact. 07/29/22 – The vendor acknowledged the report. 09/20/22 – The vendor states the vulnerability report was marked as spam by support, and the vendor asked the ZDI to resend the report. 09/20/22 – The ZDI resent the report. 06/07/23 – The ZDI asked for an update. 06/08/23 – The vendor states that the vulnerability would be fixed in a future build. 06/08/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 06/15/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-08-10 - Vulnerability reported to vendor
- 2023-06-15 - Coordinated public release of advisory
