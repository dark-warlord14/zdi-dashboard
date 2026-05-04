# ZDI-18-944: Microsoft Exchange Server Voicemail Transcription Improper Access Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-944
- **ZDI-CAN:** ZDI-CAN-6106
- **Date:** 2018-08-14
- **CVE:** CVE-2018-8302
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-944/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the conversion of voicemails to text. Due to improper access control, an attacker who has access to a voicemail-enabled Exchange account can install alternative software to be invoked for voicemail transcription. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8302

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
