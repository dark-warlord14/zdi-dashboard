# ZDI-24-672: (0Day) Deep Sea Electronics DSE855 Multipart Boundary Stack-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-672
- **ZDI-CAN:** ZDI-CAN-23170
- **Date:** 2024-06-13
- **CVE:** CVE-2024-5948
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Deep Sea Electronics
- **Affected Products:** DSE855
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-672/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Deep Sea Electronics DSE855 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of multipart boundaries. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

01/21/24 – ZDI requested a vendor PSIRT contact. 01/22/24 – The vendor provided contact information. 01/23/24 – ZDI reported the vulnerability to the vendor. 02/05/24 – The vendor states the report was blocked by IT and asked ZDI to resend the report. 02/12/24 – ZDI resent the report using an alternative method. 02/13/24 – The vendor asked why we performed tests on their products. 02/13/24 – ZDI provided the vendor with additional details about the ZDI program. 02/14/24 – The vendor asked what initiated the ZDI to look at the DSE855. 02/14/24 – ZDI emphasized our intent to responsibly disclose this vulnerability to Deep Sea for remediation. The ZDI also offered additional resources about coordinated vulnerability disclosure, as well as feedback on implementing a proper incident response process. We also reiterated our 120-day disclosure policy to ensure the vendor was aware they needed to respond with a patch within the allotted time. 05/24/24 – ZDI informed the vendor that since we never received a response that we have assume this vulnerability remains unpatched, and that we’re publishing this case as a zero-day advisory on 06/13/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2024-01-23 - Vulnerability reported to vendor
- 2024-06-13 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
