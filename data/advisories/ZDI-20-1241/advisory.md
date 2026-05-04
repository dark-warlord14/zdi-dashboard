# ZDI-20-1241: Trend Micro Antivirus for Mac Error Message Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1241
- **ZDI-CAN:** ZDI-CAN-11048
- **Date:** 2020-10-14
- **CVE:** CVE-2020-25778
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Antivirus for Mac
- **Credit:** Cees Elzinga from Danish Cyber Defence
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1241/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Antivirus for Mac. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the KERedirect kext. The issue results from an error message that includes sensitive information. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-09948

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-10-14 - Coordinated public release of advisory
