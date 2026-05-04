# ZDI-20-1026: (0Day) Horde Groupware Webmail Edition Kronolith show_time Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1026
- **ZDI-CAN:** ZDI-CAN-10445
- **Date:** 2020-08-19
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Horde
- **Affected Products:** Groupware Webmail Edition
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1026/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Horde Groupware Webmail Edition. Authentication is required to exploit this vulnerability. The specific flaw exists within Kronolith.php. When parsing the show_time parameter, the process does not properly validate user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/13/20 – ZDI reported the vulnerabilities to the vendor 07/07/20 – ZDI requested an update 07/09/20 – The vendor indicated they were working on a fix 07/09/20 – ZDI requested an ETA for the fix 07/09/20 – The vendor indicated that they could not specify a date 07/10/20 – ZDI indicated that it would provide a 2 week extension 07/21/20 – ZDI requested an update 07/31/20 – ZDI requested an update 08/13/20 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 08/18/20 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-03-13 - Vulnerability reported to vendor
- 2020-08-19 - Coordinated public release of advisory
