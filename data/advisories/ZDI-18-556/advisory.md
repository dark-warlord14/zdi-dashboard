# ZDI-18-556: Samsung Email EML File Parsing Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-556
- **ZDI-CAN:** ZDI-CAN-5328
- **Date:** 2018-06-07
- **CVE:** CVE-2018-10497
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** Email
- **Credit:** Tencent Keen Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-556/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Samsung Email. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of EML files. The issue results from the lack of proper validation of user-supplied data, which can allow arbitrary JavaScript to execute. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

Market Update / 2018 Feb SMR O os: Patched with newest Samsung Email(5.0.02.16) in Store N os: Patched with newest Samsung Email(4.2.66.2) in Store M: Patched with 2018 FEB SMR

## Disclosure Timeline

- 2017-11-05 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
