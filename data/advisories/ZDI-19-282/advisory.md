# ZDI-19-282: (0Day) (Pwn2Own) Google Android Contacts Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-282
- **ZDI-CAN:** ZDI-CAN-7471
- **Date:** 2019-03-15
- **CVE:** N/A
- **CVSS:** 5.9
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Google
- **Affected Products:** Android
- **Credit:** MWR Labs - Georgi Geshev and Robert Miller
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-282/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Google Android. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of installed applications. The issue lies in the lack of proper validation of a package prior to calling a method within it. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/14/18 - ZDI reported vulnerability to vendor 11/14/18 - Vendor acknowledged 01/27/19 - ZDI contacted vendor requesting a status update 02/06/19 - ZDI contacted vendor again requesting a status update 02/06/19 - Vendor replied stating they plan to publish an update by the end of February 02/08/19 - ZDI notified the vendor the case would be 0-dayed if a fix was not available by the end of February 03/04/19 - Vendor replied but did not provide ETA 03/06/19 - ZDI notified the vendor the intention to 0-day the reports -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-03-15 - Coordinated public release of advisory
- 2020-01-15 - Advisory Updated
