# ZDI-21-1212: Schneider Electric ConneXium Network Manager Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1212
- **ZDI-CAN:** ZDI-CAN-13656
- **Date:** 2021-10-19
- **CVE:** CVE-2021-22801
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** ConneXium Network Manager
- **Credit:** David Yesland
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1212/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric ConneXium Network Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of CXN files. The product UI does not warn the user of unsafe actions. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-287-01 https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2021-285-02

## Disclosure Timeline

- 2021-05-13 - Vulnerability reported to vendor
- 2021-10-19 - Coordinated public release of advisory
