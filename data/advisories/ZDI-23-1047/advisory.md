# ZDI-23-1047: (0Day) Inductive Automation Ignition ParameterVersionJavaSerializationCodec Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1047
- **ZDI-CAN:** ZDI-CAN-20290
- **Date:** 2023-08-08
- **CVE:** CVE-2023-39475
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Rocco Calvi (@TecR0c) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ParameterVersionJavaSerializationCodec class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

03/10/23 – ZDI reported the vulnerability to the vendor. 03/13/23 – The vendor acknowledged the report. 07/18/23 – The ZDI asked for an update. 08/01/23 – The vendor states the case is under development, but cannot provide a timeline for a fix. 08/01/23 – ZDI informed the vendor that the case will be published as a zero-day advisory on 08/08/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-03-10 - Vulnerability reported to vendor
- 2023-08-08 - Coordinated public release of advisory
- 2023-08-08 - Advisory Updated
