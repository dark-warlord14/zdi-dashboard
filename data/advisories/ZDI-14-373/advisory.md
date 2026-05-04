# ZDI-14-373: Trend Micro InterScan Web Security Virtual Appliance Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-373
- **ZDI-CAN:** ZDI-CAN-2369
- **Date:** 2014-11-06
- **CVE:** CVE-2014-8510
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security
- **Credit:** Brandon Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-373/
## Vulnerability Details

This vulnerability allows remote attackers to read files from the underlying operating system on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance web application authentication is required to exploit this vulnerability. The specific flaw exists within multiple areas of the AdminUI. The issue lies in the handling of configuration input due to a failure to safely sanitize user data before saving filters. An attacker could leverage this vulnerability to read any file to which the web app has read access.

## Additional Details

Vendor has released a hotfix to address the issue: IWSVA 6.0 HF build 1244

## Disclosure Timeline

- 2014-06-12 - Vulnerability reported to vendor
- 2014-11-06 - Coordinated public release of advisory
