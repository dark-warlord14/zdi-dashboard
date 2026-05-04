# ZDI-19-583: (0Day) Alibaba Alipay URL Scheme Handling Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-583
- **ZDI-CAN:** ZDI-CAN-6995
- **Date:** 2019-06-27
- **CVE:** N/A
- **CVSS:** 4.5
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Alibaba
- **Affected Products:** Alipay
- **Credit:** lilang wu, moony Li and yuchen zhou of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-583/
## Vulnerability Details

This vulnerability allows local attackers to modify requests on affected installations of Alibaba Alipay. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of URL schemes. The issue resides in the improper validation if a URL Scheme was acted upon by a malicious application. An attacker can leverage this vulnerability to steal tokens and manipulate requests in the context of current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch due to lack of vendor response. 08/31/18 - ZDI reported vulnerability to vendor 01/25/19 - ZDI contacted vendor requesting a status update 01/27/19 - Vendor replied stating they had missed it and requested to send it again. 01/29/19 - ZDI notified the vendor the report would be sent again. 03/07/19 - ZDI contacted vendor requesting a status update 04/01/19 - ZDI contacted vendor requesting a status update and confirmed the case would be published as 0-day. 06/25/19 - ZDI notified vendor the case would be published as 0-day on June 27th. -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-08-31 - Vulnerability reported to vendor
- 2019-06-27 - Coordinated public release of advisory
