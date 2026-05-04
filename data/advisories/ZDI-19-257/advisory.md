# ZDI-19-257: (0Day) Advantech WebAccess Node Product Installation File Access Control Modification Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-257
- **ZDI-CAN:** ZDI-CAN-7411
- **Date:** 2019-03-07
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Fritz Sands of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-257/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Advantech WebAccess Node. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the access control that is set and modified during the installation of the product. The product installation weakens existing access control restrictions of current system files, then sets weak access control restrictions on new files. An attacker can leverage this vulnerability to escalate privileges to the level of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 11/01/18 – ZDI sent the vulnerability report to ICS-CERT 11/05/18 – The vendor replied with tracking number 12/19/18 – ICS-CERT advised ZDI the vendor was working on a fix 01/22/19 – ZDI wrote ICS-CERT and indicated we saw a new build publish for this product on 1/10/19 and asked if this fix was included 01/23/19 – ICS-CERT indicated they requested an updated status from the vendor 02/15/19 – ZDI requested a status update from ICS-CERT 02/18/19 – ICS-CERT advised ZDI only that Advantech is working on a fix 02/18/19 – ZDI requested any ETA 02/18/19 – ICS-CERT agreed to request an ETA from the vendor 02/20/19 – ZDI notified the vendor if these are not patched that the reports will be published as 0-day on 03/07/19 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-11-01 - Vulnerability reported to vendor
- 2019-03-07 - Coordinated public release of advisory
- 2019-05-30 - Advisory Updated
