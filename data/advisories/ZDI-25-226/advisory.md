# ZDI-25-226: (Pwn2Own) Samsung Galaxy S24 Gaming Hub Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-226
- **ZDI-CAN:** ZDI-CAN-25581
- **Date:** 2025-04-09
- **CVE:** CVE-2024-49419 , CVE-2024-49418
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S24
- **Credit:** Ken Gannon of NCC Group (@yogehi)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-226/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Samsung Galaxy S24 smartphones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Gaming Hub application. The issue results from the lack of proper validation of a user-supplied URL. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary script in the context of a WebView.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb?year=2024&month=12

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
