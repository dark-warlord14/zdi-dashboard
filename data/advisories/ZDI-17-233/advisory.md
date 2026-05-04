# ZDI-17-233: Trend Micro InterScan Web Security Virtual Appliance transparent_setting CRLF Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-233
- **ZDI-CAN:** ZDI-CAN-4437
- **Date:** 2017-03-30
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-233/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within transparent_setting. The issue results from the lack of proper validation of a user-supplied string before using it to modify a system configuration file. An attacker can leverage this vulnerability to bypass system authentication.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116960

## Disclosure Timeline

- 2017-01-19 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
