# ZDI-19-520: Hewlett Packard Enterprise Intelligent Management Center WebSocket Shape3DWebSocketServlet Expression Language Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-520
- **ZDI-CAN:** ZDI-CAN-6804
- **Date:** 2019-05-30
- **CVE:** CVE-2019-11950
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Matthias Kaiser and Steven Seeley of Incite Team (Source Incite)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-520/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of websocket requests by the Shape3DWebSocketServlet servlet. When parsing a request the process does not properly validate a user-supplied string before using it to render a page. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docLocale=en_US&docId=emr_na-hpesbhf03930en_us&withFrame

## Disclosure Timeline

- 2019-02-05 - Vulnerability reported to vendor
- 2019-05-30 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
