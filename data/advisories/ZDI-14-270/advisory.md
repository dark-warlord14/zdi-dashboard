# ZDI-14-270: (0Day) (Pwn2Own\Pwn4Fun) Microsoft Internet Explorer localhost Protected Mode Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-270
- **ZDI-CAN:** ZDI-CAN-2209
- **Date:** 2014-07-30
- **CVE:** CVE-2014-1762
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** AbdulAziz Hariri of HP Zero Day Initiative Matt Molinyawe of HP Zero Day Initiative Jasiel Spelman of HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-270/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ability to trick the broker into loading a malicious page in a privileged context. The issue lies in the implicit trust of navigating to localhost. An attacker can leverage this vulnerability along with proxy shellcode to execute code under the context of the current user at medium integrity.

## Additional Details

This vulnerability is being disclosed publicly without a patch because vendor indicates that the vulnerability does not meet the bar for security servicing. 03/12/2014 - ZDI disclosed to vendor at Pwn2Own/Pwn4Fun 03/12/2014 - Vendor acknowledged receipt 06/10/2014 - Vendor indicated to ZDI that the case "does not meet the bar for security servicing" 06/11/2014 - ZDI indicated disagreement and intent to 0-day 06/13/2014 - Vendor requested additional evidence 06/13/2014 - ZDI replied with the requested evidence 06/13/2014 - Vendor requested ZDI hold public disclosure 07/11/2014 - Vendor indicated to ZDI that the case "does not meet the bar for security servicing" 07/14/2014 - ZDI indicated intent to 0-day 07/30/2014 - Public release of advisory -- Vendor Mitigation: * Enable Enhanced Protected Mode. For Internet Explorer 10 on Windows 8 or Internet Explorer 11 on Windows 8.1, users can help protect against exploitation of this vulnerability by changing the Advanced Security settings for Internet Explorer. You can do this by enabling Enhanced Protected Mode (EPM) settings in your browser. * To enable EPM in Internet Explorer, perform the following steps: - On the Internet Explorer Tools menu, click Internet Options. - In the Internet Options dialog box, click the Advanced tab, and then scroll down to the Security section of the settings list. - Ensure the checkbox next to Enable Enhanced Protected is selected. - Click OK to accept the changes and return to Internet Explorer. - Restart your system.

## Disclosure Timeline

- 2014-03-12 - Vulnerability reported to vendor
- 2014-07-30 - Coordinated public release of advisory
